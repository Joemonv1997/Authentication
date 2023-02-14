import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import 'bootstrap/dist/css/bootstrap.min.css';

function Login() {
    const [username,setUsername]=useState("")
    const [password,setPassword]=useState("")
    const onSubmitHandler=(e)=>{
        e.preventDefault()
        fetch('http://127.0.0.1:5001/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username,password})
        }).then(res => res.json())
        .then(res => console.log(res));
    }
  return (
    <>
    <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Username</Form.Label>
        <Form.Control type="text" placeholder="Enter username" value={username} onChange={(e)=>{
            setUsername(e.target.value)
        }} />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Enter Password" value={password} onChange={(e)=>{
            setPassword(e.target.value)
        }}/>
      </Form.Group>
      <Button variant="primary" type="submit" onClick={onSubmitHandler}>
        Submit
      </Button>
    </Form></>
  );
}

export default Login;