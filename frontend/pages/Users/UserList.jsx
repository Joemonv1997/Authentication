import { useEffect,useState } from 'react'

function UserList() {
  const [userlist,setUserlist]=useState([]);
  useEffect(()=>{
    fetch("http://127.0.0.1:5000/userslist")
    .then(res=>res.json())
    .then(data=>setUserlist(data.data));
  },[])
  
  
  return (
    <>
      <h1>List of all Users</h1>
      {userlist? userlist.map(user => (
        <div key={user.id}>
          <h2>
            Name: {user.username}
          </h2>
        </div>
      )):<h1>NO Users Available</h1>
    }
      </>
  );
}

export default UserList;