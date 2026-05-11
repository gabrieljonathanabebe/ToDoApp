// mytodo/clients/web/src/hooks/useInlineTextEdit.js

import { useState } from "react";


export function useInlineTextEdit(initialValue, onSave) {
  const [isEditing, setIsEditing] = useState(false)
  const [editValue, setEditValue] = useState('')

  function startEditing() {
    setEditValue(initialValue ?? '')
    setIsEditing(true)
  }

  function cancelEditing() {
    setEditValue(initialValue ?? '')
    setIsEditing(false)
  }

  async function saveEditing() {
    const trimmed = editValue.trim()
    if (!trimmed) {
      cancelEditing()
      return
    }
    if (trimmed === initialValue) {
      setIsEditing(false)
      return
    }
    await onSave(trimmed)
    setIsEditing(false)
  }

  return {
    isEditing,
    editValue,
    setEditValue,
    startEditing,
    cancelEditing,
    saveEditing,
  }
}
