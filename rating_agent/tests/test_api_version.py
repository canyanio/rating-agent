def test_api_rollback_transaction_graphql(client):
    response = client.post(
        "/graphql",
        json={
            "query": """
query {
    version
}"""
        },
    )
    assert response.status_code == 200
    expected = {"version": 1}
    assert response.json()["data"] == expected
