// mytodo/clients/web/src/components/task/TaskCard.jsx

import TaskStatusToggle from './TaskStatusToggle'
import TaskPriorityStars from './TaskPriorityStars'
import TaskMeta from './TaskMeta'
import InlineTextEditor from '../ui/InlineTextEditor'
import TaskCardActions from './TaskCardActions'
import Badge from '../ui/Badge'
import { taskStatusConfig } from '../../config/taskConfig'


function TaskCard({
  task,
  onDeleteTask,
  onToggleStatus,
  onUpdateTaskDescription,
  onUpdateTaskPriority,
  onUpdateTaskDue
}) {
  const status = taskStatusConfig[task.status]

  return (
    <div className='task-card'>
      <div className='task-card__status'>
        <TaskStatusToggle task={task} onToggleStatus={onToggleStatus} />
      </div>

      <div className='task-card__main'>
        <InlineTextEditor
          as='h3'
          value={task.description}
          onSave={(nextDescription) =>
            onUpdateTaskDescription(task.id, nextDescription)
          }
          displayClassName='task-card-title'
          inputClassName='task-card-input'
        />

        <TaskMeta
          task={task}
          onUpdateTaskDue={onUpdateTaskDue}
          className='task-card-meta task-meta-row'
          showSeparator={true}
        />

        <div className='task-card__secondary'>
          <TaskPriorityStars
            value={task.priority}
            interactive
            onChange={(newPriority) =>
              onUpdateTaskPriority(task.id, newPriority)
            }
          />

          <Badge tone={status?.tone ?? 'default'}>
            {status?.label ?? task.status}
          </Badge>
        </div>
      </div>

      <div className='task-card__actions'>
        <TaskCardActions
          task={task}
          onDeleteTask={onDeleteTask}
        />
      </div>
    </div>
  )
}

export default TaskCard
