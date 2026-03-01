def test_budget_logic(client):
    # Register
    register = client.post(
        "/api/v1/register",
        json={"email": "budget@test.com", "password": "password123"}
    )
    assert register.status_code == 200

    # Login
    login = client.post(
        "/api/v1/login",
        data={"username": "budget@test.com", "password": "password123"}
    )
    assert login.status_code == 200

    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Set budget
    budget = client.put(
        "/api/v1/budget",
        json={"monthly_budget": 500},
        headers=headers
    )
    assert budget.status_code == 200

    # Add expense over budget
    expense = client.post(
        "/api/v1/expense",
        json={"amount": 600, "description": "test"},
        headers=headers
    )
    assert expense.status_code == 200

    # Check summary
    summary = client.get(
        "/api/v1/summary",
        headers=headers
    )

    data = summary.json()

    assert data["budget_limit"] == 500
    assert data["budget_exceeded"] is True