// mytodo/clients/web/src/components/task/CreateTaskForm.jsx

import { useRef, useState } from 'react'
import { CalendarDays } from 'lucide-react'
import TaskPriorityStars from './TaskPriorityStars'
import Button from '../common/Button'
import { formatDueDate } from '../../utils/formatters'
import Surface from '../common/Surface'


function CreateTaskForm({
  description,
  onDescriptionChange,
  priority,
  onPriorityChange,
  due,
  onDueChange,
  notes,
  onNotesChange,
  onSubmit,
  error,
}) {
  const [showDetails, setShowDetails] = useState(false)

  const shouldShowDetails = showDetails || due || notes?.trim()
  const dateInputRef = useRef(null)

  function handleOpenDatePicker() {
    if (dateInputRef.current) {
      dateInputRef.current.showPicker?.()
      dateInputRef.current.focus()
    }
  }

  return (
    <Surface
      as='form'
      variant='panel'
      className='form-panel create-task-form'
      onSubmit={(e) => {
        e.preventDefault()
        onSubmit()
      }}
    >
      <div className='create-task-main-row'>
        {/* ----- DESCRIPTION INPUT ----- */}
        <input
          className='form-control form-input create-task-description'
          type='text'
          placeholder='Add a new task...'
          value={description}
          onFocus={() => setShowDetails(true)}
          onChange={(e) => onDescriptionChange(e.target.value)}
        />
        <Button type='submit'>Add Task</Button>
      </div>
      {shouldShowDetails && (
        <>
          <div className='create-task-meta-row'>
            {/* ----- PRIORITY ----- */}
            <div className='create-task-meta-group'>
              <TaskPriorityStars
                value={priority}
                interactive
                onChange={
                  (newPriority) => onPriorityChange(String(newPriority))
                }
              />
            </div>
            <span className='create-task-meta-separator' />

            {/* ----- DUE DATE ----- */}
            <div className='create-task-meta-group create-task-due-group'>
              <button
                type='button'
                className='icon-action icon-action-primary'
                onClick={handleOpenDatePicker}
                aria-label='Choose due date'
                title='Choose due date'
              >
                <CalendarDays size={16} strokeWidth={2} />
              </button>
              <span className='create-task-due-value'>
                {formatDueDate(due)}
              </span>
              <input
                ref={dateInputRef}
                className='create-task-hidden-date-input'
                type='date'
                value={due}
                onChange={(e) => onDueChange(e.target.value)}
              />
            </div>
          </div>
          <div className='create-task-notes-row'>
            <textarea
              className='form-control form-textarea create-task-notes'
              placeholder='Add notes (optional)...'
              value={notes}
              onChange={(e) => onNotesChange(e.target.value)}
              rows={3}
            />
          </div>
        </>
      )}
      {error && <p className='form-error'>{error}</p>}
    </Surface >
  )
}

export default CreateTaskForm
