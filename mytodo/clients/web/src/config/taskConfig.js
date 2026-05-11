// mytodo/clients/web/src/config/taskConfig.js

export const taskPriorityConfig = {
  high: {
    label: 'High',
    value: 3,
    tone: 'danger',
  },
  medium: {
    label: 'Medium',
    value: 2,
    tone: 'warning',
  },
  low: {
    label: 'Low',
    value: 1,
    tone: 'gray',
  },
}

export const taskPriorityOptions = Object.entries(taskPriorityConfig).map(
  ([key, config]) => ({
    key,
    ...config,
  })
)


export const taskStatusConfig = {
  open: {
    label: 'Open',
    tone: 'purple',
  },
  done: {
    label: 'Done',
    tone: 'success',
  },
  cancelled: {
    label: 'Cancelled',
    tone: 'danger',
  },
}

export const taskStatusOptions = Object.entries(taskStatusConfig).map(
  ([key, config]) => ({
    key,
    ...config,
  })
)
