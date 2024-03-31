import requests

def search_request(search_query, links_threshold=5, data_limit_per_page=10000):
    print("going to search request")

    base_url = 'http://localhost:3000/ai/search'
    
    # Prepare query parameters
    params = {
        'search_query': search_query,
        'links_threshold': links_threshold,
        'data_limit_per_page': data_limit_per_page
    }

    try:
        response = requests.get(base_url, params=params)
        response_data = response.json()
        
        if response.status_code == 200:
            return response_data['data']
        else:
            print("Error:", response_data.get('error', 'Unknown error'))
            return None
    except Exception as e:
        print("Error:", str(e))
        return str(e)