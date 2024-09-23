from src.app.common.features.help import help

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
      "name": "role"
   
   
}



def test_create__role():
    response = client.post("/service_master_admin/rbac/role/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all__role():
    response = client.get("/service_master_admin/rbac/role/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_role():
    response = client.get("/service_master_admin/rbac/role/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_role():
    response = client.put("/service_master_admin/rbac/role/update/1", json = {
     "name": "role one"
    })
    assert response.status_code == 200
    assert response.json() == {   
     "name": "role one"
    }

def test_delete__role():
    response = client.delete("/service_master_admin/rbac/role/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
    "name": "role one"
    }
#Testing
    

    

