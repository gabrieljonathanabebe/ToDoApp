// mytodo/clients/web/src/pages/HomePage.jsx

import Widget from '../components/widgets/Widget'
import {
  getOverviewStats,
  getUpcomingTasks,
  getRecentlyUpdatedToDos,
} from '../analytics/metrics'
import {
  formatDueDate,
  formatDaysLeft,
} from '../utils/formatters'
import { House, History, ListTodo } from 'lucide-react'
import PageHeader from '../components/common/PageHeader'
import KpiWidget from '../components/widgets/KpiWidget'
import ToDoLists from '../components/todo/ToDoLists'
import EmptyState from '../components/common/EmptyState'


function HomePage({
  currentUser,
  workspaceStats,
  toDoSummaries = [],
  toDoDetails = [],
  onOpenToDo,
}) {
  const overview = getOverviewStats(
    workspaceStats,
    toDoSummaries,
    toDoDetails
  )
  const upcomingTasks = getUpcomingTasks(toDoDetails, 3)
  const recentTodos = getRecentlyUpdatedToDos(toDoSummaries, 3)
  const overviewItems = [
    {
      label: 'Open tasks',
      value: overview.openTasks,
    },
    {
      label: 'Done tasks',
      value: overview.doneTasks,
    },
    {
      label: 'Overdue tasks',
      value: overview.overdueTasks,
      tone: 'danger',
    },
    {
      label: 'To-do lists',
      value: overview.totalToDos,
    },
  ]

  return (
    <div className='home-page'>
      <PageHeader title='Home' icon={House} />
      <div className='home-grid'>
        <Widget
          title={`Welcome back, ${currentUser?.username ?? 'there'}`}
          subtitle={
            <>
              <span>Here is a quick overview of your current workspace.</span>
              <span>Stay focused on upcoming and overdue work.</span>
            </>
          }
          className='home-widget home-widget-welcome'
        />
        <KpiWidget
          title='Overview'
          subtitle='Your most important numbers at a glance'
          className='home-widget home-widget-overview'
          items={overviewItems}
        />
        {/* ===== UPCOMING TASKS ========================================== */}
        <Widget
          title='Upcoming tasks'
          subtitle='What needs attention next'
          className='home-widget home-widget-upcoming'
        >
          {upcomingTasks.length === 0 ? (
            <p className='home-muted-text'>No upcoming tasks with due dates.</p>
          ) : (
            <div className='home-list'>
              {upcomingTasks.map((task) => (
                <div key={`${task.toDoId}-${task.id}`} className='home-list-item'>
                  <div className='home-list-main'>
                    <div className='home-list-title'>{task.description}</div>
                    <div className='home-list-subtitle'>
                      {formatDueDate(task.due)} · {formatDaysLeft(task.days_left)}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </Widget>
      </div>
      <section className='home-section'>
        <PageHeader
          title='Recently updated lists'
          icon={History}
          variant='section'
          as='h2'
        />
        {recentTodos.length === 0 ? (
          <EmptyState
            icon={ListTodo}
            title='No recent list activity'
            description='Updated lists will appear here once you start working.'
          />
        ) : (
          <ToDoLists
            todos={recentTodos}
            onOpenToDo={onOpenToDo}
          />
        )}
      </section>
    </div>
  )
}

export default HomePage
