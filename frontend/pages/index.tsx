import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
import { useEffect, useState } from 'react'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const [basic,setBasic]=useState('')
  useEffect(()=>{
    fetch("http://127.0.0.1:5000/")
    .then(res=>res.json())
    .then(data=>setBasic(data));
  },[])
  return (
    <>
      <h1>Flask React NextJS Project</h1>
      <h1>API Response was {basic['hello']}</h1>
    </>
  )
}
