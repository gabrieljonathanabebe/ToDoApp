// mytodo/clients/web/src/components/layout/Header.jsx

import Surface from "../common/Surface"
import Button from "../common/Button"
import Brand from "../common/Brand"


function Header({ currentUser, onLogout, onGoHome }) {
  return (
    <Surface as="header" variant="bar" className="app-header">
      {/* ===== BRAND ===================================================== */}
      <button
        type="button"
        className="app-brand-button"
        onClick={onGoHome}
        aria-label="Go to home"
        title="Go to home"
      >
        <Brand />
      </button>
      {/* ===== ACTIONS =================================================== */}
      {currentUser && (
        <Button onClick={onLogout}>Logout</Button>
      )}
    </Surface>
  )
}

export default Header
