from rating_agent.tests.common import EngineTestingQueue


def test_api_rollback_transaction_rest(client, engine):
    _ = engine
    EngineTestingQueue.put({'ok': True})
    response = client.post(
        "/v1/rollback_transaction",
        json=dict(
            tenant='default',
            transaction_tag='100',
            account_tag='1000',
            destination_account_tag='1001',
        ),
    )
    assert response.status_code == 200
    assert response.json() == {
        'ok': True,
        'tenant': 'default',
        'transaction_tag': '100',
        'account_tag': '1000',
        'destination_account_tag': '1001',
    }


def test_api_rollback_transaction_graphql(client, engine):
    _ = engine
    EngineTestingQueue.put({'ok': True})
    response = client.post(
        "/graphql",
        json={
            "query": """
mutation {
    rollbackTransaction(
        tenant: "default",
        transaction_tag: "100",
        account_tag: "1000",
        destination_account_tag: "1001"
    ) {
        ok
        tenant
        transaction_tag
        account_tag
        destination_account_tag
    }
}"""
        },
    )
    assert response.status_code == 200
    expected = {
        "rollbackTransaction": {
            "ok": True,
            "tenant": "default",
            "transaction_tag": "100",
            "account_tag": "1000",
            "destination_account_tag": "1001",
        }
    }
    assert response.json()["data"] == expected
