// mytodo/clients/web/src/pages/DashboardPage.jsx

import PageHeader from '../components/common/PageHeader'
import {
  getOverviewStats,
  getStatusBreakdown,
  getPriorityBreakdown,
  getAverageLeadTime,
  getMostActiveToDos,
} from '../analytics/metrics'
import { formatDuration } from '../utils/formatters'
import { LayoutDashboard } from 'lucide-react'
import KpiWidget from '../components/widgets/KpiWidget'
import BreakdownWidget from '../components/widgets/BreakdownWidget'


function DashboardPage({
  workspaceStats,
  toDoSummaries = [],
  toDoDetails = [],
}) {
  const overview = getOverviewStats(
    workspaceStats,
    toDoSummaries,
    toDoDetails
  )
  const statusBreakdown = getStatusBreakdown(toDoDetails)
  const priorityBreakdown = getPriorityBreakdown(toDoDetails)
  const averageLeadTime = getAverageLeadTime(toDoDetails)
  const mostActiveToDos = getMostActiveToDos(toDoDetails, 3)
  const totalStatusCount =
    statusBreakdown.open + statusBreakdown.done || 1

  const totalPriorityCount =
    priorityBreakdown.low +
    priorityBreakdown.medium +
    priorityBreakdown.high || 1

  const completionRate =
    overview.totalTasks > 0
      ? Math.round((overview.doneTasks / overview.totalTasks) * 100)
      : 0

  const overviewItems = [
    {
      label: 'Total tasks',
      value: overview.totalTasks,
    },
    {
      label: 'Completion rate',
      value: `${completionRate}%`,
    },
    {
      label: 'Average lead time',
      value: averageLeadTime != null ? formatDuration(averageLeadTime) : '-',
    },
    {
      label: 'Overdue tasks',
      value: overview.overdueTasks,
      tone: 'danger',
    },
  ]

  function toPercent(value, total) {
    return Math.round((value / total) * 100)
  }

  const statusItems = [
    {
      label: 'Open',
      value: statusBreakdown.open,
      percent: toPercent(statusBreakdown.open, totalStatusCount),
      percentLabel: `${toPercent(statusBreakdown.open, totalStatusCount)}%`,
      tone: 'open',
    },
    {
      label: 'Done',
      value: statusBreakdown.done,
      percent: toPercent(statusBreakdown.done, totalStatusCount),
      percentLabel: `${toPercent(statusBreakdown.done, totalStatusCount)}%`,
      tone: 'success',
    },
  ]

  const priorityItems = [
    {
      label: 'Low',
      value: priorityBreakdown.low,
      percent: toPercent(priorityBreakdown.low, totalPriorityCount),
      percentLabel: `${toPercent(priorityBreakdown.low, totalPriorityCount)}%`,
      tone: 'low',
    },
    {
      label: 'Medium',
      value: priorityBreakdown.medium,
      percent: toPercent(priorityBreakdown.medium, totalPriorityCount),
      percentLabel: `${toPercent(priorityBreakdown.medium, totalPriorityCount)}%`,
      tone: 'medium',
    },
    {
      label: 'High',
      value: priorityBreakdown.high,
      percent: toPercent(priorityBreakdown.high, totalPriorityCount),
      percentLabel: `${toPercent(priorityBreakdown.high, totalPriorityCount)}%`,
      tone: 'danger',
    },
  ]

  const mostActiveItems = mostActiveToDos.map((toDo) => {
    const percent =
      toDo.totalTasks > 0
        ? toPercent(toDo.openTasks, toDo.totalTasks)
        : 0

    return {
      label: toDo.title,
      value: `${toDo.openTasks}/${toDo.totalTasks}`,
      percent,
      percentLabel: `${percent}% open`,
      tone: 'open',
    }
  })


  return (
    <div className='dashboard-page'>
      {/* ===== PAGE TITLE ================================================ */}
      <PageHeader title='Dashboard' icon={LayoutDashboard} />

      {/* ===== DASHBOARD GRID ============================================ */}
      <div className='dashboard-grid'>
        {/* ===== KPI OVERVIEW ============================================ */}
        <KpiWidget
          title='Overview'
          subtitle='Your key metrics at a glance'
          className='dashboard-widget dashboard-widget-overview'
          items={overviewItems}
        />

        {/* ===== STATUS BREAKDOWN ======================================== */}
        <BreakdownWidget
          title='Status breakdown'
          subtitle='Open versus completed work'
          className='dashboard-widget dashboard-widget-status'
          items={statusItems}
        />
        {/* ===== PRIORITY BREAKDOWN ====================================== */}
        <BreakdownWidget
          title='Priority breakdown'
          subtitle='Distribution across low, medium and high'
          className='dashboard-widget dashboard-widget-priority'
          items={priorityItems}
        />
        <BreakdownWidget
          title='Most active lists'
          subtitle='Lists with the highest amount of open work'
          className='dashboard-widget dashboard-widget-active-lists'
          items={mostActiveItems}
          emptyText='No active lists yet.'
        />
      </div>
    </div>
  )
}

export default DashboardPage
