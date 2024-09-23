from src.app.common.features.help import help

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
       "permission_id": 1,
       "role_id": 1
   
   
}



def test_create__role_has_permission():
    response = client.post("/service_master_admin/rbac/role_has_permission/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all__role_has_permission():
    response = client.get("/service_master_admin/rbac/role_has_permission/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_role_has_permission():
    response = client.get("/service_master_admin/rbac/role_has_permission/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_role_has_permission():
    response = client.put("/service_master_admin/rbac/role_has_permission/update/1", json = {
     "permission_id": 2,
      "role_id": 1
    })
    assert response.status_code == 200
    assert response.json() == {   
     "permission_id": 2,
     "role_id": 1
    }

def test_delete__role_has_permission():
    response = client.delete("/service_master_admin/rbac/role_has_permission/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
    "permission_id": 2,
    "role_id": 1
    }

    

    
#Testing
