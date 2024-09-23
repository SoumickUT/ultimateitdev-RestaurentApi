#Testing
from src.app.common.features.help import help

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
    "title": "IsaiahT-Tech",
    "description": "Today",
    "read_status": True
}




def test_create_todo():
    response = client.post("/service_student_admin/manage/help/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all_todo():
    response = client.get("/service_student_admin/manage/help/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_todo():
    response = client.get("/service_student_admin/manage/help/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_todo():
    response = client.put("/service_student_admin/manage/help/update/1", json = {
        "title": "Test",
        "description": "Python"
    })
    assert response.status_code == 200
    assert response.json() == {   
        "title": "Test",
        "description": "Python"
    }

def test_delete_todo():
    response = client.delete("/service_student_admin/manage/help/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
        "title": "Test",
        "description": "Python"
    }

    

    

