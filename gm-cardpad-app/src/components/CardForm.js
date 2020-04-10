import React from 'react'
import ReactDOM from 'react-dom'
import { useForm } from 'react-hook-form'

export default function CardForm(props) {
  const { register, handleSubmit, watch, errors } = useForm()
  const onSubmit = data => { 
    console.log("Adding card for card-id:" + props['card-id'])    
    console.log(data) 
    }

  console.log(watch('example')) // watch input value by passing the name of it

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
        <input name="title" placeholder="Card Title" ref={register({required:true})}/>
        <textarea name="content" ref={register({required:true})}/>
        <input name="tags" placeholder="Tags (seperate with commas)" ref={register()}/>
        {errors.exampleRequired && <span>This field is required</span>}
        <input type="submit"/>
    </form>
    
  )
}