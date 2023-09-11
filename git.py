import streamlit as st
from memory import mem
from fetch import fetch_p
from main import get_pdf_text, get_text_chunks, namesp



st.title("Echo Bot")

# Object notation
with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=False)
        book_n = st.text_input('Book Name')
        st.write('Book Name:', book_n)

        name_sp = st.text_input('Name Space')
        st.write('Name Sapce:', name_sp)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)


                # create vector store
                namesp(text_chunks,name_sp,book_n)

                st.write("success")


                

        if st.button("Use Existing Doc"):
             with st.spinner("Processing"):


                st.write("success")



                  


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": f"You can ask anything from book {book_n}"}]
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

cnt=0
# React to user input
if prompt := st.chat_input("Hii dbot here to code"):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    doc=fetch_p(prompt,name_sp)
    response=mem(f"""Answer the question: {prompt} based on the information: {doc}. If the question cannot be answered using the information provided then answer it irrespective of the information.""")
    st.chat_message("assistant").markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})