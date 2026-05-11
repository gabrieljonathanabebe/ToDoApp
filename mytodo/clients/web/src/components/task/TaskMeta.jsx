// mytodo/clients/web/src/components/task/TaskMeta.jsx

import { Timer } from 'lucide-react'
import { formatDaysLeft } from '../../utils/formatters'
import DueDateEditor from './DueDateEditor'


function TaskMeta({
  task,
  onUpdateTaskDue,
  className = '',
  showSeparator = true,
}) {
  function getDaysLeftTone(daysLeft) {
    if (daysLeft == null) return ''
    if (daysLeft < 0) return 'meta-item--danger'
    if (daysLeft === 0) return 'meta-item--warning'
    return ''
  }

  return (
    <div className={className}>
      <span className='meta-item'>
        <DueDateEditor
          value={task.due}
          onChange={(newDue) => onUpdateTaskDue(task.id, newDue)}
        />
      </span>
      {showSeparator && (
        <span className='meta-separator'>|</span>
      )}
      <span className={`meta-item ${getDaysLeftTone(task.days_left)}`}>
        <Timer className='meta-icon' size={14} strokeWidth={2} />
        {formatDaysLeft(task.days_left)}
      </span>
    </div>
  )
}

export default TaskMeta
