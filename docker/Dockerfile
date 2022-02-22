FROM maduprey/conftopo-core

# Expose port 8501 for Streamlit app (http://localhost:8501/)
EXPOSE 8501

# Add new non-root user
RUN groupadd -g 1001 appuser && \
    useradd -r -m -u 1001 -g appuser appuser \
    && chown -hR appuser:appuser /conftopo/ \
    && chmod -R 777 /conftopo
USER appuser

WORKDIR /conftopo

CMD streamlit run run_conftopo.py