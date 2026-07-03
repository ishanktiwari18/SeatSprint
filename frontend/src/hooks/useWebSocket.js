import { useEffect, useRef, useState } from 'react'
import ReconnectingWebSocket from 'reconnecting-websocket'

export default function useWebSocket(url) {
  const socketRef = useRef(null)
  const [lastMessage, setLastMessage] = useState(null)

  useEffect(() => {
    const token = localStorage.getItem('access_token')
    const fullUrl = `${import.meta.env.VITE_WS_BASE_URL || 'ws://localhost:8000'}${url}?token=${token}`
    const socket = new ReconnectingWebSocket(fullUrl)
    socket.onmessage = (event) => setLastMessage(JSON.parse(event.data))
    socketRef.current = socket
    return () => socket.close()
  }, [url])

  return { lastMessage }
}
