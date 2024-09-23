from src.app.common.features.help import help
#Testing
from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
    "title": "IsaiahT-Tech",
    "description": "Today",
    "read_status": True
   
}



def test_create_report():
    response = client.post("/service_student_admin/manage/report_problem/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all_report():
    response = client.get("/service_student_admin/manage/report_problem/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_report():
    response = client.get("/service_student_admin/manage/report_problem/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_report():
    response = client.put("/service_student_admin/manage/report_problem/update/1", json = {
    "title": "IsaiahT-Tech",
    "description": "Today",
    "read_status": True
    })
    assert response.status_code == 200
    assert response.json() == {   
    "title": "IsaiahT-Tech",
    "description": "Today",
    "read_status": True
    }

def test_delete_report():
    response = client.delete("/service_student_admin/mareport_problem/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
    "title": "IsaiahT-Tech",
    "description": "Today",
    "read_status": True
    }

    

    

