from src.app.common.features.help import help

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
       "esjusers_id": 1,
       "group_id": 1
   
   
}



def test_create__group_has_user():
    response = client.post("/service_master_admin/rbac/group_has_user/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all__group_has_user():
    response = client.get("/service_master_admin/rbac/group_has_user/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_group_has_user():
    response = client.get("/service_master_admin/rbac/group_has_user/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_group_has_user():
    response = client.put("/service_master_admin/rbac/group_has_user/update/1", json = {
     "esjusers_id": 2,
     "group_id": 1
    })
    assert response.status_code == 200
    assert response.json() == {   
     "esjusers_id": 2,
     "group_id": 1
    }

def test_delete__group_has_user():
    response = client.delete("/service_master_admin/rbac/group_has_user/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
    "esjusers_id": 2,
    "group_id": 1
    }

    

    #Testing

