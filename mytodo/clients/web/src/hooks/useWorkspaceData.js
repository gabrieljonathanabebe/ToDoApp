// mytodo/clients/web/src/hooks/useWorkspaceData.js


import { useState } from "react";
import { fetchToDoSummaries } from "../api/toDoSummary";
import { fetchToDoDetail } from "../api/toDoDetail";


const EMPTY_WORKSPACE = {
  todo_summaries: [],
  todos: [],
  stats: null,
}


export function useWorkspaceData() {
  const [workspace, setWorkspace] = useState(EMPTY_WORKSPACE)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  function setWorkspaceState(nextWorkspace) {
    setWorkspace(nextWorkspace ?? EMPTY_WORKSPACE)
  }

  // ===== LOAD FULL WORKSPACE ================================================
  async function loadWorkspace(user) {
    if (!user) return
    setLoading(true)
    setError('')

    try {
      const summaries = await fetchToDoSummaries(user.username)
      const todos = await Promise.all(
        summaries.map((todo) => fetchToDoDetail(user.username, todo.id))
      )

      setWorkspaceState({
        todo_summaries: summaries,
        todos,
        stats: null
      })
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  // ===== CLEAR ==============================================================
  function clearWorkspace() {
    setWorkspaceState(null)
    setError('')
    setLoading(false)
  }


  return {
    workspace,
    loading,
    error,
    loadWorkspace,
    setWorkspaceState,
    clearWorkspace,
  }
}
