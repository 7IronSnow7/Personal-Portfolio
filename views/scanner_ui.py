import streamlit as st
from forms.streamlit_app import *
from io import StringIO
import pandas as pd

st.title("Web Security Scanner 🔍")

# Disclaimer
st.markdown("### ⚠️ Disclaimer")
st.warning("""
**Important:** This security scanner is a tool designed for educational and ethical use. 
- **Do not use this tool to scan any website without proper authorization.**
- Scanning websites without explicit permission is **illegal** and can result in severe legal consequences.
- Always obtain written consent from the website owner before conducting a scan.

By using this tool, you agree to take full responsibility for your actions.
""")


target_url = st.text_input("Enter the URL to scan:", placeholder="https://example.com")
max_depth = st.number_input("Maximum Crawl Depth:", min_value=1, max_value=3, value=3)

# Explanation of Maximum Depth
with st.expander("What does 'Maximum Crawl Depth' mean?"):
    st.markdown("""
    **Maximum Depth** defines how many levels deep the scanner will crawl through the website's links:
    
    - **Depth 1**: Only the base URL (e.g., `https://example.com`).
    - **Depth 2**: Links found on the base URL's page (e.g., `https://example.com/page1`, `https://example.com/page2`).
    - **Depth 3**: Links found on pages discovered in Depth 2, and so on.
    
    **Why is this important?**
    - It controls the scope and performance of the scan.
    - Prevents the scanner from endlessly crawling deep or unrelated sections of the site.
    - Focuses on the most relevant areas of the site.

    Learn more about web crawling and security scanning concepts in [this article](https://searchengineland.com/manage-crawl-depth-better-seo-performance-428542#:~:text=Crawl%20depth%20refers%20to%20the,or%20any%20other%20starting%20point.)).
    """)

if st.button("Start Scan"):
    if target_url:
        st.write(f"Scanning: {target_url} with max depth {max_depth}...")
        scanner = WebSecurityScanner(target_url, max_depth)
        vulnerabilities = scanner.scan()

        if vulnerabilities:
            st.error(f"Vulnerabilities Found: {len(vulnerabilities)}")
            
            vulnerabilities_df = pd.DataFrame(vulnerabilities)
            vulnerabilities_df.index += 1
            
            # Display vulnerabilities in a table
            for i, row in vulnerabilities_df.iterrows():
                    st.markdown(f"### {i}. Vulnerability Details")
                    st.write(f"**Type:** {row['type']}")
                    st.write(f"**URL:** {row['url']}")
                    st.write(f"**Information Type:** {row['info_type']}")
                    st.write(f"**Detected Value (Pattern Match):** `{row['pattern']}`")  # Displays the actual sensitive data
                    st.divider()
            
            # Export to CSV
            csv = vulnerabilities_df.to_csv(index_label="Index")
            csv_bytes = csv.encode('utf-8')
            st.download_button(
                label="Download Vulnerabilities as CSV",
                data=csv_bytes,
                file_name="vulnerabilities.csv",
                mime="text/csv",
            )
        else:
            st.success("No vulnerabilities found.")
    else:
        st.warning("Please enter a valid URL.")
        
    # List of vulnerabilities that could of been found    
    remedies = {
        "Sensitive Information Exposure": "Review your website's content and remove any sensitive information like email addresses or phone numbers. If necessary, restrict sensitive data exposure using authentication or obfuscation techniques.",
        "Unsecured Cookies": "Ensure all cookies are set with the 'Secure' flag and are transmitted over HTTPS. Use the 'HttpOnly' flag to prevent client-side access.",
        "Outdated Software": "Update your web server, frameworks, and libraries to the latest secure versions.",
        "XSS Vulnerability": "Sanitize and validate all user inputs. Use Content Security Policies (CSP) to mitigate XSS risks.",
    }
    
    # Display remediation advice
    remedy = remedies.get(row["type"], "No specific remedy available for this vulnerability type.")
    st.markdown(f"**Recommended Remedy:** {remedy}")
    st.divider()  # Visual divider

    if row["type"] == "Outdated Software":
        st.markdown(f"**Recommended Remedy:** Update the software at {row['url']} to the latest version.")
        
    remedy_links = {
        "Sensitive Information Exposure": "https://owasp.org/www-community/attacks/Sensitive_Data_Exposure",
        "XSS Vulnerability": "https://owasp.org/www-community/attacks/xss/",
    }
    link = remedy_links.get(row["type"], "")
    if link:
        st.markdown(f"**Learn More:** [OWASP Guide](https://www.parasoft.com/blog/sensitive-data-exposure-owasp-top-10/)")
    
    # Maybe add in an email feature
    # Need to fix the views page