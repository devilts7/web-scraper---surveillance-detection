import os
from flask import Flask, render_template, request, redirect, url_for, Response, jsonify

from scraper import WebScraper

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret-key')

scraper_instances = {}

def get_scraper(stealth=True):
    key = f"stealth_{stealth}"
    if key not in scraper_instances:
        scraper_instances[key] = WebScraper(timeout=30, retries=3, rate_limit=1.0, stealth=stealth)
    return scraper_instances[key]

scraper = get_scraper(stealth=True)


@app.route('/')
def index():
    url = request.args.get('url', '')
    return render_template('index.html', 
                         url=url, 
                         result=None, 
                         error=None,
                         history=scraper.get_history(),
                         stats=scraper.get_stats())


@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        stealth = request.form.get('stealth') == 'on'
        deep_scan = request.form.get('deep_scan') == 'on'
        extract_meta = request.form.get('extract_meta') == 'on'
        follow_links = request.form.get('follow_links') == 'on'
    else:
        url = request.args.get('url', '').strip()
        stealth = True
        deep_scan = False
        extract_meta = True
        follow_links = False
    
    if not url:
        return render_template('index.html', 
                             url='', 
                             result=None, 
                             error='// ERROR: No target URL specified',
                             history=scraper.get_history(),
                             stats=scraper.get_stats())
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        active_scraper = get_scraper(stealth=stealth)
        active_scraper.stealth = stealth
        
        result = active_scraper.scrape_page(url, deep_scan=deep_scan)
        
        result['options'] = {
            'stealth': stealth,
            'deep_scan': deep_scan,
            'extract_meta': extract_meta,
            'follow_links': follow_links
        }
        
        error = None
        if result.get('bot_protection') or result.get('requires_auth'):
            error = result.get('error')
        
        return render_template('index.html', 
                             url=url, 
                             result=result, 
                             error=error,
                             history=active_scraper.get_history(),
                             stats=active_scraper.get_stats())
    except Exception as e:
        return render_template('index.html', 
                             url=url, 
                             result=None, 
                             error=f'// EXCEPTION: {str(e)}',
                             history=scraper.get_history(),
                             stats=scraper.get_stats())


@app.route('/export/json')
def export_json():
    url = request.args.get('url', '')
    
    history = scraper.get_history()
    result = None
    for item in reversed(history):
        if item.get('url') == url:
            result = item
            break
    
    if result is None and history:
        result = history[-1]
    
    if result:
        json_data = scraper.export_to_json(result)
        return Response(
            json_data,
            mimetype='application/json',
            headers={'Content-Disposition': 'attachment; filename=phantom_scrape.json'}
        )
    
    return redirect(url_for('index'))


@app.route('/export/csv')
def export_csv():
    url = request.args.get('url', '')
    
    history = scraper.get_history()
    result = None
    for item in reversed(history):
        if item.get('url') == url:
            result = item
            break
    
    if result is None and history:
        result = history[-1]
    
    if result:
        csv_data = scraper.export_to_csv(result)
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=phantom_scrape.csv'}
        )
    
    return redirect(url_for('index'))


@app.route('/api/scrape')
def api_scrape():
    url = request.args.get('url', '').strip()
    stealth = request.args.get('stealth', 'true').lower() == 'true'
    deep_scan = request.args.get('deep_scan', 'false').lower() == 'true'
    
    if not url:
        return jsonify({'error': 'URL parameter is required', 'code': 'NO_TARGET'}), 400
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    active_scraper = get_scraper(stealth=stealth)
    result = active_scraper.scrape_page(url, deep_scan=deep_scan)
    return jsonify(result)


@app.route('/api/stats')
def api_stats():
    return jsonify(scraper.get_stats())


@app.route('/api/history')
def api_history():
    limit = request.args.get('limit', 10, type=int)
    history = scraper.get_history()[-limit:]
    return jsonify({'history': history, 'total': len(scraper.get_history())})


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['X-Powered-By'] = 'Phantom Scraper v2.0'
    return response


if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
