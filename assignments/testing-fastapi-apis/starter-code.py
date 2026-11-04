import main
import pytest
from fastapi.testclient import TestClient

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_task_store():
    main.tasks.clear()
    main.next_task_id = 1


def test_list_tasks_returns_empty_list():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task_returns_created_task():
    # TODO: Send a valid POST request and check its status and response body.
    pytest.fail("Implement the task creation test")


def test_get_task_returns_matching_task():
    # TODO: Create a task, request its ID, and check the returned task.
    pytest.fail("Implement the task lookup test")


def test_update_task_returns_updated_task():
    # TODO: Create a task, update it, and check the response and new values.
    pytest.fail("Implement the task update test")


def test_delete_task_returns_no_content():
    # TODO: Create a task, delete it, and check the response and final state.
    pytest.fail("Implement the task deletion test")


def test_missing_task_endpoints_return_not_found():
    # TODO: Check GET, PUT, and DELETE using an ID that does not exist.
    pytest.fail("Implement the not-found tests")


def test_create_task_without_title_returns_unprocessable_entity():
    # TODO: Send a POST request without the required title field.
    pytest.fail("Implement the request validation test")