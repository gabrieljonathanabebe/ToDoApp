// mytodo/clients/web/src/selectors/workspaceSelectors.js


export function getSummaries(workspace) {
  return workspace?.todo_summaries ?? []
}


export function getToDos(workspace) {
  return workspace?.todos ?? []
}


export function getStats(workspace) {
  return workspace?.stats ?? null
}


export function getToDoById(workspace, toDoId) {
  if (!toDoId) return null
  return getToDos(workspace).find((todo) => todo.id === toDoId) ?? null
}


export function getSummaryById(workspace, todoId) {
  if (!todoId) return null
  return getSummaries(workspace).find((todo) => todo.id === todoId) ?? null
}
