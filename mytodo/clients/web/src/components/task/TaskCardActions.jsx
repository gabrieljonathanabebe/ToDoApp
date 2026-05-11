// mytodo/clients/web/src/components/task/TaskCardActions.jsx

import { useState } from 'react'

import TaskActionsMenu from './TaskActionsMenu'
import TaskInfoModal from './TaskInfoModal'

function TaskCardActions({ task, onDeleteTask }) {
  const [showInfo, setShowInfo] = useState(false)

  return (
    <div className='task-card-actions'>
      <TaskActionsMenu
        onDelete={() => onDeleteTask(task.id)}
        onOpenInfo={() => setShowInfo(true)}
      />
      <TaskInfoModal
        show={showInfo}
        onClose={() => setShowInfo(false)}
        task={task}
      />
    </div>
  )
}

export default TaskCardActions
