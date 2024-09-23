from src.app.common.features.help import help

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
      "name": "Permission"
   
   
}



def test_create__permission():
    response = client.post("/service_master_admin/rbac/permission/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all__permission():
    response = client.get("/service_master_admin/rbac/permission/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_permission():
    response = client.get("/service_master_admin/rbac/permission/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_permission():
    response = client.put("/service_master_admin/rbac/permission/update/1", json = {
     "name": "Permission one"
    })
    assert response.status_code == 200
    assert response.json() == {   
     "name": "Permission one"
    }

def test_delete__permission():
    response = client.delete("/service_master_admin/rbac/permission/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
    "name": "Permission one"
    }

    #Testing

    

