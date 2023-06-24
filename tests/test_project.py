
def test_get_word(client):
    response = client.get('/api/word')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'TEST'

def test_admin_portal(client):
    response = client.get('/admin')
    assert response.status_code == 200
    assert b'Admin Portal' in response.data

def test_update_word(client):
    new_word = 'Updated'
    response = client.post('/admin', data={'new_Word': new_word})
    assert response.status_code == 302
    print(response.headers['Location'])
    assert response.headers['Location'] == '/admin'
    
    response = client.get('/api/word')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == new_word