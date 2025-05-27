import {useEffect, useState} from 'react'
import axios from 'axios'


const fruits = ['apple','banana','orange','mango']


function App(){
  const [counts,setCounts] = useState({})

  const fetchCounts = async()=>{
    const res = await axios.get("http://localhost:5000/counts")
    setCounts(res.data)
  }
  
  const handleClick = async(fruit)=>{
    await axios.post(`http://localhost:5000/click/${fruit}`)
    fetchCounts()
  }

  useEffect(()=>{
    fetchCounts()
  },[])
  return (
    <div style={{ textAlign:'center' }}>
      <h2>Fruit Click Counter</h2>
      <div style={{ display: 'flex', justifyContent: 'center', gap: '20px', flexWrap: 'wrap', marginTop: '20px' }}>
        {fruits.map(fruit => (
          <button key={fruit} onClick={() => handleClick(fruit)} style={{ padding: '10px 20px' }}>
            {fruit} ({counts[fruit] || 0})
          </button>
          ))}
      </div>
    </div>
  )
}

export default App