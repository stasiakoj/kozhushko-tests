import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_get_emojis(github_api):
    r = github_api.get_emojis()
    assert r['ukraine'] != None

@pytest.mark.api
def test_repo_list_commits_size(github_api):
    r = github_api.list_commits('sergii-butenko', 'become-qa-auto-aug2020')
    assert len(r) > 0

@pytest.mark.api
def test_repo_list_commits_message(github_api):
    r = github_api.list_commits('sergii-butenko', 'become-qa-auto-aug2020')
    assert r[-1]['commit']['message'] == 'Initial commit'
