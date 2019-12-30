from rating_agent.tests.common import EngineTestingQueue


def test_api_begin_transaction_rest(client, engine):
    _ = engine
    EngineTestingQueue.put({'ok': True})
    response = client.post(
        "/v1/begin_transaction",
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
    assert response.json() == {'ok': True}


def test_api_begin_transaction_graphql(client, engine):
    _ = engine
    EngineTestingQueue.put({'ok': True})
    response = client.post(
        "/graphql",
        json={
            "query": """
mutation {
    beginTransaction(
        tenant: "default",
        transaction_tag: "100",
        account_tag: "1000",
        destination_account_tag: "1001",
        source: "sip:10.0.0.1:5060",
        destination: "sip:10.0.0.2:5060"
    ) {
        ok
    }
}"""
        },
    )
    assert response.status_code == 200
    expected = {"beginTransaction": {"ok": True}}
    assert response.json()["data"] == expected
