// mytodo/clients/web/src/hooks/useToDoSummaryActions.js

import { useState } from "react";
import { createToDo, deleteToDo } from "../api/toDoSummary";


export function useToDoSummaryActions(
  currentUser,
  setWorkspaceState,
  onOpenToDo
) {
  const [error, setError] = useState('')
  const [newTitle, setNewTitle] = useState('')
  const [createError, setCreateError] = useState('')

  async function handleCreateToDo() {
    setCreateError('')
    if (!newTitle.trim()) {
      setCreateError('Please enter a title.')
      return
    }
    try {
      const title = newTitle.trim()
      const workspace = await createToDo(currentUser.username, title)
      setWorkspaceState(workspace)
      setNewTitle('')
      const createdToDo = workspace.todo_summaries.find(
        (todo) => todo.title === title
      )
      if (createdToDo) {
        onOpenToDo?.(createdToDo)
      }
    } catch (err) {
      setCreateError(err.message)
    }
  }

  async function handleDeleteToDo(todoId) {
    const confirmed = window.confirm('Do you really want to delete this To-Do?')
    if (!confirmed) return
    setError('')
    try {
      const workspace = await deleteToDo(currentUser.username, todoId)
      setWorkspaceState(workspace)
    } catch (err) {
      setError(err.message)
    }
  }

  return {
    error,
    newTitle,
    setNewTitle,
    createError,
    handleCreateToDo,
    handleDeleteToDo,
  }
}
