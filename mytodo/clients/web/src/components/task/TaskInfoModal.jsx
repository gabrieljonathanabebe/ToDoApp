// mytodo/clients/web/src/components/task/TaskInfoModal.jsx

import Modal from '../common/Modal'
import TaskAdvancedMeta from './TaskAdvancedMeta'

function TaskInfoModal({ show, onClose, task }) {
  return (
    <Modal
      open={show}
      title='Task details'
      onClose={onClose}
      labelledBy={`task-info-title-${task.id}`}
    >
      <TaskAdvancedMeta task={task} />
    </Modal>
  )
}

export default TaskInfoModal
