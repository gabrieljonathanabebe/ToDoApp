// mytodo/clients/web/src/components/common/LoadingState.jsx

import { LoaderCircle } from "lucide-react";
import Surface from "./Surface"


function LoadingState({
  title = 'Loading...', message = 'Please wait a moment.'
}) {
  return (
    <Surface variant="panel" className="state-card">
      <div className="state-icon-wrap">
        <LoaderCircle
          className="state-icon state-icon-spin" size={28} strokeWidth={2}
        />
      </div>
      <h2 className="state-title">{title}</h2>
      <p className="state-description">{message}</p>
    </Surface>
  )
}

export default LoadingState
