import React from 'react'
function postmethod(body){
    return fetch(`http://127.0.0.1:5000/register`,{
        'method':"POST",
        headers:{
            'Content-Type':'applications/json'
        },
        body:JSON.stringify(body)
    })
    .then(res=>res.json())
    .then(data=>console.log(data));
}
function ApiServices() {

  return (
    <div>ApiServices</div>
  )
}

export default ApiServices