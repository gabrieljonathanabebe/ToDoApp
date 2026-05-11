// mytodo/clients/web/src/components/task/TaskGridCard.jsx

import Surface from '../common/Surface'
import TaskStatusToggle from './TaskStatusToggle'
import TaskMeta from './TaskMeta'
import TaskPriorityStars from './TaskPriorityStars'
import InlineTextEditor from '../ui/InlineTextEditor'
import TaskCardActions from './TaskCardActions'


function TaskGridCard({
  task,
  onDeleteTask,
  onToggleStatus,
  onUpdateTaskDescription,
  onUpdateTaskPriority,
  onUpdateTaskDue,
}) {

  return (
    <Surface
      as='article'
      variant='card'
      interactive
      className='task-grid-card'
    >
      <div className='task-grid-card__header'>
        <TaskStatusToggle task={task} onToggleStatus={onToggleStatus} />
        <TaskCardActions
          task={task}
          onDeleteTask={onDeleteTask}
        />
      </div>
      <div className='task-grid-card__body'>
        <InlineTextEditor
          as='h3'
          value={task.description}
          onSave={(nextDescription) =>
            onUpdateTaskDescription(task.id, nextDescription)
          }
          displayClassName='task-grid-card__title'
          inputClassName='task-grid-card__input'
        />
      </div>
      <div className='task-grid-card__footer'>
        <div className='task-grid-card__badges'>
          <TaskPriorityStars
            value={task.priority}
            interactive
            onChange={(newPriority) =>
              onUpdateTaskPriority(task.id, newPriority)
            }
          />
        </div>
        <TaskMeta
          task={task}
          onUpdateTaskDue={onUpdateTaskDue}
          className='task-grid-card__meta task-meta-row'
          showSeparator={false}
        />
      </div>
    </Surface >
  )
}

export default TaskGridCard
