import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import 'bootstrap/dist/css/bootstrap.min.css';

import React from 'react'

function Register() {
    const [username,setUsername]=useState("")
    const [email,setEmail]=useState("")
    const [password,setPassword]=useState("")
    const onSubmitHandler=(e)=>{
        e.preventDefault()
        fetch('http://127.0.0.1:5001/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username,email,password})
        }).then(res => res.json())
        .then(res => console.log(res));
    }
  return (
    <div>
        <Form>
      <Form.Group className="mb-3" controlId="formusername">
        <Form.Label>Username</Form.Label>
        <Form.Control type="text" placeholder="Enter username" value={username} onChange={(e)=>{
            setUsername(e.target.value)
        }} />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email Address</Form.Label>
        <Form.Control type="email" placeholder="Enter EmailAddress" value={email} onChange={(e)=>{
            setEmail(e.target.value)
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
    </Form>
    </div>
  )
}

export default Register