// mytodo/clients/web/src/components/todo/CreateToDoForm.jsx

import Button from "../common/Button"
import Surface from "../common/Surface"


function CreateToDoForm({ title, onTitleChange, onSubmit, error }) {
  return (
    <Surface
      as="form"
      variant="panel"
      className="form-panel"
      onSubmit={(e) => {
        e.preventDefault()
        onSubmit()
      }}
    >
      <div className="form-row">
        <input
          className="form-control form-input"
          type="text"
          placeholder="New Todo"
          value={title}
          onChange={(e) => onTitleChange(e.target.value)}
        />

        <Button type="submit">Add</Button>
      </div>

      {error && <p className="form-error">{error}</p>}
    </Surface>
  )
}

export default CreateToDoForm
