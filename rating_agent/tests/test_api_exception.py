import pytest  # type: ignore

from rating_agent.tests.common import EngineTestingQueue


def test_api_exception_rest(client, engine):
    _ = engine
    EngineTestingQueue.put(ValueError('test'))
    with pytest.raises(RuntimeError):
        client.post(
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


def test_api_exception_graphql(client, engine):
    _ = engine
    EngineTestingQueue.put(ValueError('test'))
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
    assert response.status_code == 400
    expected = {"authorization": None}
    assert response.json()["data"] == expected
