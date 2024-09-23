from src.app.common.features.help import help

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
     "group_id": 1,
     "role_id": 1
   
   
}



def test_create__Group_has_role():
    response = client.post("/service_master_admin/rbac/group_has_role/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all__Group_has_role():
    response = client.get("/service_master_admin/rbac/group_has_role/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_Group_has_role():
    response = client.get("/service_master_admin/rbac/group_has_role/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_Group_has_role():
    response = client.put("/service_master_admin/rbac/group_has_role/update/1", json = {
     "group_id": 2,
     "role_id": 2
    })
    assert response.status_code == 200
    assert response.json() == {   
     "group_id": 2,
     "role_id": 2
    }

def test_delete__Group_has_role():
    response = client.delete("/service_master_admin/rbac/group_has_role/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
    "group_id": 2,
    "role_id": 2
    }

    #Testing

    

