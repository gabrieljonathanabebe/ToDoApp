// mytodo/clients/web/src/components/common/ErrorState.jsx

import { AlertCircle } from "lucide-react";
import Surface from "./Surface"


function ErrorState({
  title = 'Something went wrong',
  message = 'An unexpected error occurred. Please try again.'
}) {
  return (
    <Surface variant="panel" className="state-card">
      <div className="state-icon-wrap">
        <AlertCircle
          className="state-icon state-icon-danger"
          size={28}
          strokeWidth={2}
        />
      </div>
      <h2 className="state-title">{title}</h2>
      <p className="state-description">{message}</p>
    </Surface>
  )
}

export default ErrorState
