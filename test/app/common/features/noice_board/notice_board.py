#Testing
from src.app.common.features.help import help

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
    "notice_title": "IsaiahT-Tech",
    "notice_description": "Today",
    "notice_url": "String",
    "is_notice_active": True,
    "notice_start_date_and_time": "2022-08-10T16:28:20.699Z",
    "notice_end_date_and_time": "2022-08-10T16:28:20.699Z"


}




def test_create_notice():
    response = client.post("/service_student_admin/manage/notice/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all_notice():
    response = client.get("/service_student_admin/manage/notice/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_notice():
    response = client.get("/service_student_admin/manage/notice/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_notice():
    response = client.put("/service_student_admin/manage/notice/update/1", json = {
    "notice_title": "Tech",
    "notice_description": "Today",
    "notice_url": "String",
    "is_notice_active": True,
    "notice_start_date_and_time": "2022-08-10T16:28:20.699Z",
    "notice_end_date_and_time": "2022-08-10T16:28:20.699Z"
    })
    assert response.status_code == 200
    assert response.json() == {   
    "notice_title": "Tech",
    "notice_description": "Today",
    "notice_url": "String",
    "is_notice_active": True,
    "notice_start_date_and_time": "2022-08-10T16:28:20.699Z",
    "notice_end_date_and_time": "2022-08-10T16:28:20.699Z"
    }

def test_delete_notice():
    response = client.delete("/service_student_admin/manage/notice/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
    "notice_title": "Tech",
    "notice_description": "Today",
    "notice_url": "String",
    "is_notice_active": True,
    "notice_start_date_and_time": "2022-08-10T16:28:20.699Z",
    "notice_end_date_and_time": "2022-08-10T16:28:20.699Z"
    }

    

    

