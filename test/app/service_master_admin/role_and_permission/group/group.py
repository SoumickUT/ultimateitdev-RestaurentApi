from src.app.common.features.help import help

from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
    "g_name": "IsaiahT-Tech"
   
   
}



def test_create__Group():
    response = client.post("/service_master_admin/rbac/group/create", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all__Group():
    response = client.get("/service_master_admin/rbac/group/get_all", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_Group():
    response = client.get("/service_master_admin/rbac/group/get_one/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_Group():
    response = client.put("/service_master_admin/rbac/group/update/1", json = {
    "g_name": "Tech"
    })
    assert response.status_code == 200
    assert response.json() == {   
    "g_name": "Tech"
    }

def test_delete__Group():
    response = client.delete("/service_master_admin/rbac/delete/1")
    assert response.status_code == 200
    assert response.json() == {   
    "g_name": "Tech"
    }
#Testing
    

    

