from cognata_api.web_api.cognata_demo import CognataRequests


def get_api(username="apiuser", password="Aa123456", company_id="2a4ab8d2"):
    """
    Args:
        username (str, optional): Cognata Studio Username. Defaults to "apiuser".
        password (str, optional): Cognata Studio Password. Defaults to "Aa123456".
        company_id (str, optional): Cognata Studio Company ID. Defaults to "2a4ab8d2".

    Raises:
        ValueError: Either username or password are wrong

    Returns:
        CognataRequests: the API object that makes the request to Cognata 
    """
    connection = CognataRequests(
        f"https://{company_id}-api.cognata-studio.com/v1", username, password)
    if not connection.is_logged_in:
        raise ValueError("Either username / password is wrong.")
    return connection

# def start(api: CognataRequests):
#     # maps = api.get_maps_list(lite=True)
#     # print('maps',maps)
    
#     answer = api._perform_get_request(f'{api.client_api_url}/catalog/aicar')
#     print('answer', answer)
#     pass

def start(api: CognataRequests):
    
    answer = api._perform_get_request(f'{api.client_api_url}/catalog/asset/')
    print('answer', answer)
    pass


# /catalog/intensityTable


def main():
    # staert a connections  
    api = get_api()
    start(api)


if __name__ == '__main__':
    main()
