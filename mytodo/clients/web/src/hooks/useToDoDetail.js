// mytodo/clients/web/src/hooks/useToDoDetail.js

import { useState } from 'react'
import {
  createTask,
  deleteTask,
  updateTaskStatus,
  updateTaskOrder,
  updateTaskDescription,
  updateTaskPriority,
  updateTaskDue,
} from '../api/toDoDetail'


export function useToDoDetail(
  currentUser,
  currentToDo,
  initialToDoDetail,
  setWorkspaceState,
) {
  const toDoDetail = initialToDoDetail ?? null
  const [error, setError] = useState('')
  const [description, setDescription] = useState('')
  const [priority, setPriority] = useState('2')
  const [due, setDue] = useState('')
  const [notes, setNotes] = useState('')
  const [createError, setCreateError] = useState('')


  // ===== HANDLE CREATE TASK ============================================
  async function handleCreateTask() {
    setCreateError('')

    if (!description.trim()) {
      setCreateError('Please enter a description.')
      return
    }

    try {
      const workspace = await createTask(currentUser.username, currentToDo.id, {
        description: description.trim(),
        priority: Number(priority),
        due: due || null,
        notes: notes?.trim() ? notes : null,
      })
      setWorkspaceState(workspace)
      setDescription('')
      setPriority('2')
      setDue('')
      setNotes('')
    } catch (err) {
      setCreateError(err.message)
    }
  }

  // ===== HANDLE DELETE TASK ============================================
  async function handleDeleteTask(taskId) {
    const confirmed = window.confirm('Do you really want to delete this task?')
    if (!confirmed) return

    try {
      const workspace = await deleteTask(
        currentUser.username, currentToDo.id, taskId
      )
      setWorkspaceState(workspace)
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE TOGGLE TASK STATUS =====================================
  async function handleToggleTaskStatus(task) {
    let newStatus

    if (task.status === 'open') {
      newStatus = 'done'
    } else if (task.status === 'done') {
      newStatus = 'open'
    } else {
      newStatus = 'open'
    }

    try {
      const workspace = await updateTaskStatus(
        currentUser.username,
        currentToDo.id,
        task.id,
        newStatus
      )
      setWorkspaceState(workspace)
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE SORT TASKS =============================================
  function compareTasksBy(key) {
    const priorityWeight = {
      low: 1,
      medium: 2,
      high: 3,
    }
    return (left, right) => {
      if (key === 'due') {
        if (!left.due && !right.due) return 0
        if (!left.due) return 1
        if (!right.due) return -1
        return new Date(left.due) - new Date(right.due)
      }
      if (key === 'priority') {
        return (priorityWeight[left.priority] ?? 0) -
          (priorityWeight[right.priority] ?? 0)
      }
      return String(left[key] ?? '').localeCompare(
        String(right[key] ?? '')
      )
    }
  }


  async function handleSortTasks(key, reverse = false) {
    try {
      const sortedTasks = [...(toDoDetail?.tasks ?? [])]
        .sort(compareTasksBy(key))
      if (reverse) {
        sortedTasks.reverse()
      }
      const items = sortedTasks.map((task, index) => ({
        id: task.id,
        position: index + 1,
      }))
      const workspace = await updateTaskOrder(
        currentUser.username,
        currentToDo.id,
        items
      )
      setWorkspaceState(workspace)
    } catch (err) {
      setError(err.message)
    }
  }



  // ===== HANDLE UPDATE TASK DESCRIPTION ================================
  async function handleUpdateTaskDescription(taskId, description) {
    try {
      const workspace = await updateTaskDescription(
        currentUser.username,
        currentToDo.id,
        taskId,
        description
      )
      setWorkspaceState(workspace)
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE UPDATE TASK PRIORITY ===================================
  async function handleUpdateTaskPriority(taskId, priority) {
    try {
      const workspace = await updateTaskPriority(
        currentUser.username,
        currentToDo.id,
        taskId,
        priority
      )
      setWorkspaceState(workspace)
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE UPDATE TASK DUE ========================================
  async function handleUpdateTaskDue(taskId, newDue) {
    try {
      const workspace = await updateTaskDue(
        currentUser.username,
        currentToDo.id,
        taskId,
        newDue
      )
      setWorkspaceState(workspace)
    } catch (err) {
      setError(err.message)
    }
  }

  return {
    toDoDetail,
    error,
    description,
    setDescription,
    priority,
    setPriority,
    due,
    setDue,
    notes,
    setNotes,
    createError,
    handleCreateTask,
    handleDeleteTask,
    handleToggleTaskStatus,
    handleSortTasks,
    handleUpdateTaskDescription,
    handleUpdateTaskPriority,
    handleUpdateTaskDue,
  }
}
