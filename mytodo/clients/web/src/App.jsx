// mytodo/clients/web/src/App.jsx

import AppShell from './components/layout/AppShell'
import LoginPage from './pages/LoginPage'
import HomePage from './pages/HomePage'
import ToDoSummaryPage from './pages/ToDoSummaryPage'
import DashboardPage from './pages/DashboardPage'
import ToDoDetailPage from './pages/toDoDetail/ToDoDetailPage'
import {
	getSummaries,
	getToDos,
	getToDoById,
	getSummaryById,
	getStats
} from './selectors/workspaceSelectors'
import { useWorkspaceData } from './hooks/useWorkspaceData'
import { useNavigationState } from './hooks/useNavigationState'
import { useSessionState } from './hooks/useSessionState'
import { useEffect } from 'react'


function App() {
	// ===== HOOKS ==========================================================
	const { currentUser, loginUser, logoutUser } = useSessionState()
	const {
		page, currentToDoId, navigateTo, openToDo, clearNavigation
	} = useNavigationState()

	const {
		workspace,
		loading,
		error,
		loadWorkspace,
		setWorkspaceState,
		clearWorkspace,
	} = useWorkspaceData()

	const toDoSummaries = getSummaries(workspace)
	const toDoDetails = getToDos(workspace)
	const currentToDo = getSummaryById(workspace, currentToDoId)
	const currentToDoDetail = getToDoById(workspace, currentToDoId)
	const workspaceStats = getStats(workspace)


	function handleLogin(user) {
		loginUser(user)
		navigateTo('home')
	}

	function handleLogout() {
		logoutUser()
		clearWorkspace()
		navigateTo('login')
	}

	useEffect(() => {
		if (currentUser) {
			loadWorkspace(currentUser)
		} else {
			clearWorkspace()
		}
	}, [currentUser])

	const shellProps = {
		currentUser,
		currentPage: page,
		currentToDo,
		toDoSummaries,
		onGoHome: () => navigateTo('home'),
		onGoSummary: () => navigateTo('summary'),
		onGoDashboard: () => navigateTo('dashboard'),
		onOpenToDo: openToDo,
		onLogout: handleLogout,
	}

	function renderPageContent() {
		if (page === 'home') {
			return (
				<HomePage
					currentUser={currentUser}
					workspaceStats={workspaceStats}
					toDoSummaries={toDoSummaries}
					toDoDetails={toDoDetails}
				/>
			)
		}

		if (page === 'summary') {
			return (
				<ToDoSummaryPage
					currentUser={currentUser}
					todos={toDoSummaries}
					loading={loading}
					error={error}
					setWorkspaceState={setWorkspaceState}
					onOpenToDo={openToDo}
				/>
			)
		}

		if (page === 'dashboard') {
			return (
				<DashboardPage
					currentUser={currentUser}
					workspaceStats={workspaceStats}
					toDoSummaries={toDoSummaries}
					toDoDetails={toDoDetails}
				/>
			)
		}

		if (page === 'detail') {
			return (
				<ToDoDetailPage
					currentUser={currentUser}
					currentToDo={currentToDo}
					initialToDoDetail={currentToDoDetail}
					setWorkspaceState={setWorkspaceState}
				/>
			)
		}

		return null
	}

	if (page === 'login') {
		return <LoginPage onLogin={handleLogin} />
	}

	return <AppShell {...shellProps}>{renderPageContent()}</AppShell>
}

export default App
