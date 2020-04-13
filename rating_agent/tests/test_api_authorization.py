from rating_agent.tests.common import EngineTestingQueue


def test_api_authorization_rest(client, engine):
    _ = engine
    EngineTestingQueue.put({'authorized': True})
    response = client.post(
        "/v1/authorization",
        json=dict(
            tenant='default',
            transaction_tag='100',
            account_tag='1000',
            destination_account_tag='1001',
            source='sip:10.0.0.1:5060',
            destination='sip:10.0.0.2:5060',
        ),
    )
    assert response.status_code == 200
    assert response.json() == {
        'account_tag': '1000',
        'authorized': True,
        'authorized_destination': False,
        'balance': 0,
        'carriers': [],
        'destination_account_tag': '1001',
        'max_available_units': 0,
        'tenant': 'default',
        'transaction_tag': '100',
        'unauthorized_account_tag': None,
        'unauthorized_reason': None,
    }


def test_api_authorization_graphql(client, engine):
    _ = engine
    EngineTestingQueue.put({'authorized': True})
    response = client.post(
        "/graphql",
        json={
            "query": """
mutation {
    authorization(
        tenant: "default",
        transaction_tag: "100",
        account_tag: "1000",
        destination_account_tag: "1001",
        source: "sip:10.0.0.1:5060",
        destination: "sip:10.0.0.2:5060"
    ) {
        authorized
    }
}"""
        },
    )
    assert response.status_code == 200
    expected = {"authorization": {"authorized": True}}
    assert response.json()["data"] == expected
