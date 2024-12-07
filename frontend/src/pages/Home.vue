<template>
  <div class=" mx-20">

    <div class="flex flex-row items-center justify-between">
      <h2 class="text-5xl font-black text-gray-900">Lists</h2>
      <button icon-left="plus">New List</button>
    </div>

    <div>
      <Card title="General">
        <div>
          <ul>
            <li class="flex flex-row space-y-2 items-center justify-between" v-for="action in actions.data" :key="action.title">
              <span>{{ action.title }}</span>
              <Button @click="completeAction(action.name)" icon="check"></Button>
            </li>
          </ul>
          <button @click="addActionDialogShown = true" icon-left="plus">Add Action</button>
        </div>
      </Card>
    </div>
    <Dialog 
        :options="{
            title: 'Add New Action',
            actions: [
                {
                    label: 'Add Action',
                    variant: 'solid',
                    appearance: 'primary',
                    handler: ({close}) => {
                        addAction()     // updateRole()
                        close()         // closes dialog
                    },
                },
                {
                    label: 'Cancel'
                },
            ],
        }"
        v-model="addActionDialogShown"
    >
        <template #body-content>
            <div class="space-y-2">
                <input 
                    v-model="action.title"
                    type="text" 
                    name="" 
                    id="" 
                    placeholder="Give your action a title" 
                    label="Title" 
                    required 
                />
                <input 
                    v-model="action.category"
                    type="select" 
                    label="List" 
                    :options="categoryOptions" 
                />
            </div>
            <!-- <div class="space-y-2">
                <input 
                    v-model="action.title" 
                    type="text" 
                    label="Title" 
                    placeholder="Give your action a title" 
                    required 
                />
                <input 
                    v-model="action.category"
                    type="select"
                    :label="'List'"
                    :options="categoryOptions"
                ></input>
            </div> -->
        </template>
    </Dialog>
  </div>
</template>



<script setup>
import {Dialog, createListResource, Card, Input} from 'frappe-ui';
import {reactive, ref, computed} from 'vue';

const action = reactive({
    title: '',
    category: "General",
})

const addActionDialogShown = ref(false)

const actions = createListResource({
  doctype: 'Actions',
  fields: ["name", "title", "status", "description", "date", "due_date"],
  filters: {
    status: 'ToDo',
  },
  limit: 100
})
actions.reload()

const categories = createListResource({
    doctype: 'Category',
    fields: ['name'],
    transform(categories){
        return categories.map((c) => c.name)
    },
})
categories.reload()

const categoryOptions = computed(() => {
    if (categories.list.loading || !categories.data){
        return []
    }
    return categories.data;
})

const completeAction = (actionName) => {
    actions.setValue.submit({
        name: actionName,
        status: 'Completed'
    })
}

const addAction = () => {
    actions.insert.submit(action)
}

</script>
