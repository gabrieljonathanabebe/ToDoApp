// mytodo/clients/web/src/components/ui/InlineTextEditor.jsx

import { useInlineTextEdit } from "../../hooks/useInlineTextEdit";


function InlineTextEditor({
  value,
  onSave,
  as: DisplayComponent,
  inputClassName = '',
  displayClassName = '',
  placeholder = '',
  title = 'Click to edit',
}) {
  const {
    isEditing,
    editValue,
    setEditValue,
    startEditing,
    cancelEditing,
    saveEditing,
  } = useInlineTextEdit(value, onSave)

  if (isEditing) {
    return (
      <input
        className={['editable-input', inputClassName]
          .filter(Boolean)
          .join(' ')}
        type='text'
        value={editValue}
        placeholder={placeholder}
        autoFocus
        onChange={(event) => setEditValue(event.target.value)}
        onBlur={saveEditing}
        onKeyDown={(event) => {
          if (event.key === 'Enter') {
            saveEditing()
          }
          if (event.key === 'Escape') {
            cancelEditing()
          }
        }}
      />
    )
  }

  return (
    <DisplayComponent className={displayClassName}>
      <button
        type='button'
        className='editable-field editable-field--text'
        onClick={startEditing}
        title={title}
      >
        {value}
      </button>
    </DisplayComponent>
  )
}

export default InlineTextEditor
